
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
drums = pretty_midi.Instrument(program=9)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

# Time in seconds: 4 bars at 160 BPM
# 1 bar = 6.0s, so 0.375s per beat
bar_length = 6.0
beat_length = 0.375  # seconds per beat

# --- DRUMS: Little Ray on kick and snare, hihat on every 8th note ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th

# Bar 1: Kick and snare only (setup)
for bar in [0]:
    for beat in [0, 2]:  # Kick on 1 and 3
        kick = pretty_midi.Note(velocity=100, pitch=36, start=bar * bar_length + beat * beat_length, end=bar * bar_length + beat * beat_length + 0.1)
        drums.notes.append(kick)
    for beat in [1, 3]:  # Snare on 2 and 4
        snare = pretty_midi.Note(velocity=100, pitch=38, start=bar * bar_length + beat * beat_length, end=bar * bar_length + beat * beat_length + 0.1)
        drums.notes.append(snare)

# Bar 2-4: Full rhythm
for bar in [1, 2, 3]:
    for beat in [0, 2]:  # Kick on 1 and 3
        kick = pretty_midi.Note(velocity=100, pitch=36, start=bar * bar_length + beat * beat_length, end=bar * bar_length + beat * beat_length + 0.1)
        drums.notes.append(kick)
    for beat in [1, 3]:  # Snare on 2 and 4
        snare = pretty_midi.Note(velocity=100, pitch=38, start=bar * bar_length + beat * beat_length, end=bar * bar_length + beat * beat_length + 0.1)
        drums.notes.append(snare)
    # Hi-hat on every 8th
    for eighth in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=bar * bar_length + eighth * beat_length / 2, end=bar * bar_length + eighth * beat_length / 2 + 0.05)
        drums.notes.append(hihat)

pm.instruments.append(drums)

# --- BASS: Marcus on walking line, chromatic approaches, no repeated notes ---
# Fm7 (F, Ab, Bb, C) -> root is F, but bass starts on Ab for tension

# Bar 1: Fm7 rootless walk
note_durations = [0.25, 0.25, 0.25, 0.25]

# Bar 1: Ab -> Bb -> C -> D (chromatic approach to F)
for i, note in enumerate([70, 71, 72, 74]):
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=0 + i * note_durations[i], end=0 + i * note_durations[i] + note_durations[i])
    bass.notes.append(bass_note)

# Bar 2: F -> Gb -> Ab -> Bb (chromatic approach to F)
for i, note in enumerate([53, 54, 56, 57]):
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=bar_length + i * note_durations[i], end=bar_length + i * note_durations[i] + note_durations[i])
    bass.notes.append(bass_note)

# Bar 3: C -> Db -> Eb -> F (chromatic approach to F)
for i, note in enumerate([60, 61, 63, 64]):
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=2 * bar_length + i * note_durations[i], end=2 * bar_length + i * note_durations[i] + note_durations[i])
    bass.notes.append(bass_note)

# Bar 4: F -> Gb -> Ab -> Bb
for i, note in enumerate([53, 54, 56, 57]):
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=3 * bar_length + i * note_durations[i], end=3 * bar_length + i * note_durations[i] + note_durations[i])
    bass.notes.append(bass_note)

pm.instruments.append(bass)

# --- PIANO: Diane on comping, 7th chords on 2 and 4 ---
# Fm7: F, Ab, Bb, C
# Gm7: G, Bb, C, D
# Am7: A, C, D, E
# Bbm7: Bb, D, Eb, F

# Bar 1: Rest (setup)
# Bar 2: Gm7 on 2 and 4
for bar in [1]:
    for beat in [1, 3]:
        for note in [67, 71, 72, 74]:  # G, Bb, C, D
            piano_note = pretty_midi.Note(velocity=95, pitch=note, start=bar * bar_length + beat * beat_length, end=bar * bar_length + beat * beat_length + 0.25)
            piano.notes.append(piano_note)

# Bar 3: Am7 on 2 and 4
for bar in [2]:
    for beat in [1, 3]:
        for note in [65, 72, 74, 76]:  # A, C, D, E
            piano_note = pretty_midi.Note(velocity=95, pitch=note, start=bar * bar_length + beat * beat_length, end=bar * bar_length + beat * beat_length + 0.25)
            piano.notes.append(piano_note)

# Bar 4: Bbm7 on 2 and 4
for bar in [3]:
    for beat in [1, 3]:
        for note in [71, 76, 77, 53]:  # Bb, D, Eb, F
            piano_note = pretty_midi.Note(velocity=95, pitch=note, start=bar * bar_length + beat * beat_length, end=bar * bar_length + beat * beat_length + 0.25)
            piano.notes.append(piano_note)

pm.instruments.append(piano)

# --- SAX: YOUR MOMENT. One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs. ---
# Fm7: F, Ab, Bb, C
# Motif: F (16th), Ab (eighth), rest (eighth), Bb (quarter)

# Bar 1: Start the motif
sax_note = pretty_midi.Note(velocity=110, pitch=53, start=0, end=0 + 0.1875)  # F, 16th
sax.notes.append(sax_note)

sax_note = pretty_midi.Note(velocity=110, pitch=60, start=0.1875, end=0.375)  # Ab, 8th
sax.notes.append(sax_note)

# Bar 2: Repeat motif but with space
sax_note = pretty_midi.Note(velocity=110, pitch=53, start=bar_length, end=bar_length + 0.1875)  # F, 16th
sax.notes.append(sax_note)

sax_note = pretty_midi.Note(velocity=110, pitch=60, start=bar_length + 0.1875, end=bar_length + 0.375)  # Ab, 8th
sax.notes.append(sax_note)

# Bar 3: Leave it hanging — only the Bb
sax_note = pretty_midi.Note(velocity=110, pitch=71, start=2 * bar_length, end=2 * bar_length + 0.5)  # Bb, quarter
sax.notes.append(sax_note)

# Bar 4: Return to finish it — F on the last beat, echoing the start
sax_note = pretty_midi.Note(velocity=110, pitch=53, start=3 * bar_length + 0.375, end=3 * bar_length + 0.5)  # F, 16th
sax.notes.append(sax_note)

pm.instruments.append(sax)

# Save the MIDI file
pm.write("dante_russo_intro.mid")
