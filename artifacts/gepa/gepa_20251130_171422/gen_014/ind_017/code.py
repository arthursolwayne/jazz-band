
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = []
pm.time_signature_changes.append(pretty_midi.TimeSignature(4, 4, 0.0))
pm.tempo_changes = []
pm.tempo_changes.append(pretty_midi.TempoChange(160.0, 0.0))

# Create instruments
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drum_program = pretty_midi.instrument_name_to_program('Drums')

sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drum_program)

pm.instruments = [sax, bass, piano, drums]

# Tempo and timing
BPM = 160
bar_duration = 6.0 / 4  # 6 seconds for 4 bars = 1.5 seconds per bar
beat_duration = bar_duration / 4  # 0.375 seconds per beat
note_duration = beat_duration * 0.5  # Half note = 0.75 seconds

# Bar 1: Drums only (tension)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# We'll use the MIDI note numbers for the drum kit
# MIDI note 36 = Kick, 38 = Snare, 42 = Hi-Hat

# Bar 1, 4 beats
drum_notes = [
    (36, 0.0, note_duration),       # Kick on 1
    (38, beat_duration, note_duration),  # Snare on 2
    (36, 2 * beat_duration, note_duration),  # Kick on 3
    (38, 3 * beat_duration, note_duration),  # Snare on 4
    # Hihat on every eighth
    (42, 0.0, beat_duration / 2),  # 1
    (42, beat_duration / 2, beat_duration / 2),  # &
    (42, beat_duration, beat_duration / 2),  # 2
    (42, 3 * beat_duration / 2, beat_duration / 2),  # &
    (42, beat_duration * 2, beat_duration / 2),  # 3
    (42, beat_duration * 2.5, beat_duration / 2),  # &
    (42, beat_duration * 3, beat_duration / 2),  # 4
    (42, beat_duration * 3.5, beat_duration / 2)   # &
]

for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 2-4: Full ensemble
# Key: Dm (D, F, Ab, C)
# Dm7 = D, F, Ab, C

# Bar 2: Bass and Piano
# Bass: Walking line in Dm, chromatic, no repeats
bass_notes = [
    # Bar 2
    (62, 1.5, note_duration),  # F (Dm3)
    (64, 1.5 + beat_duration, note_duration),  # G (chromatic)
    (60, 1.5 + 2 * beat_duration, note_duration),  # E (chromatic)
    (62, 1.5 + 3 * beat_duration, note_duration),  # F
    # Bar 3
    (61, 3.0, note_duration),  # E
    (63, 3.0 + beat_duration, note_duration),  # G#
    (60, 3.0 + 2 * beat_duration, note_duration),  # E
    (62, 3.0 + 3 * beat_duration, note_duration),  # F
    # Bar 4
    (64, 4.5, note_duration),  # G
    (65, 4.5 + beat_duration, note_duration),  # A
    (62, 4.5 + 2 * beat_duration, note_duration),  # F
    (64, 4.5 + 3 * beat_duration, note_duration),  # G
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4, comp only
# Dm7 = D, F, Ab, C (pitches: 62, 64, 69, 72)
piano_notes = [
    # Bar 2
    (62, 1.5 + beat_duration, note_duration),  # D
    (64, 1.5 + beat_duration, note_duration),  # F
    (69, 1.5 + beat_duration, note_duration),  # Ab
    (72, 1.5 + beat_duration, note_duration),  # C
    (62, 1.5 + 3 * beat_duration, note_duration),  # D
    (64, 1.5 + 3 * beat_duration, note_duration),  # F
    (69, 1.5 + 3 * beat_duration, note_duration),  # Ab
    (72, 1.5 + 3 * beat_duration, note_duration),  # C
    # Bar 3
    (62, 3.0 + beat_duration, note_duration),
    (64, 3.0 + beat_duration, note_duration),
    (69, 3.0 + beat_duration, note_duration),
    (72, 3.0 + beat_duration, note_duration),
    (62, 3.0 + 3 * beat_duration, note_duration),
    (64, 3.0 + 3 * beat_duration, note_duration),
    (69, 3.0 + 3 * beat_duration, note_duration),
    (72, 3.0 + 3 * beat_duration, note_duration),
    # Bar 4
    (62, 4.5 + beat_duration, note_duration),
    (64, 4.5 + beat_duration, note_duration),
    (69, 4.5 + beat_duration, note_duration),
    (72, 4.5 + beat_duration, note_duration),
    (62, 4.5 + 3 * beat_duration, note_duration),
    (64, 4.5 + 3 * beat_duration, note_duration),
    (69, 4.5 + 3 * beat_duration, note_duration),
    (72, 4.5 + 3 * beat_duration, note_duration),
]

for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Saxophone motif: One concise, melodic phrase — Dm scale, but with an emotional edge
# Dm scale: D, Eb, F, G, Ab, Bb, C (MIDI: 62, 63, 64, 65, 69, 70, 72)
# Motif: D, Eb, F, Ab, C (62, 63, 64, 69, 72) — ascending, ending on C (tension)

sax_notes = [
    (62, 1.5, note_duration),  # D
    (63, 1.5 + beat_duration, note_duration),  # Eb
    (64, 1.5 + 2 * beat_duration, note_duration),  # F
    (69, 1.5 + 3 * beat_duration, note_duration),  # Ab
    (72, 1.5 + 3 * beat_duration, note_duration),  # C
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drum continuation: Same pattern, but now with more space to let the melody breathe
# Bar 2: 4 beats, same pattern but with more space
# Skip the hihat for now to let the melody breathe
drum_notes_bar2 = [
    (36, 1.5, note_duration),       # Kick on 1
    (38, 1.5 + beat_duration, note_duration),  # Snare on 2
    (36, 1.5 + 2 * beat_duration, note_duration),  # Kick on 3
    (38, 1.5 + 3 * beat_duration, note_duration),  # Snare on 4
]

for note in drum_notes_bar2:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Same pattern
drum_notes_bar3 = [
    (36, 3.0, note_duration),       # Kick on 1
    (38, 3.0 + beat_duration, note_duration),  # Snare on 2
    (36, 3.0 + 2 * beat_duration, note_duration),  # Kick on 3
    (38, 3.0 + 3 * beat_duration, note_duration),  # Snare on 4
]

for note in drum_notes_bar3:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 4: Same pattern, but lighter
drum_notes_bar4 = [
    (36, 4.5, note_duration),       # Kick on 1
    (38, 4.5 + beat_duration, note_duration),  # Snare on 2
    (36, 4.5 + 2 * beat_duration, note_duration),  # Kick on 3
    (38, 4.5 + 3 * beat_duration, note_duration),  # Snare on 4
]

for note in drum_notes_bar4:
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Save the MIDI file
pm.write("dante_russo_intro.mid")
print("MIDI file saved as 'dante_russo_intro.mid'")
