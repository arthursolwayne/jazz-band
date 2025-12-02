
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax_instrument = pretty_midi.Instrument(program=64)
bass_instrument = pretty_midi.Instrument(program=33)
piano_instrument = pretty_midi.Instrument(program=0)
drum_instrument = pretty_midi.Instrument(program=0, is_drum=True)

# Time in seconds per bar: 6.0 seconds for 4 bars at 160 BPM
# Each bar: 1.5 seconds
# Each beat: 0.375 seconds
beat_time = 0.375
bar_time = 1.5

# ---------------------
# DRUMS: Little Ray (Bar 1: solo, Bars 2-4: full band)
# ---------------------

# Bar 1: Snare on 2 and 4, hihat on every eighth
# Kick on 1 and 3
bar1_drums = [
    (0, pretty_midi.note_number_to_name(36)),  # Kick on beat 1
    (0.375, pretty_midi.note_number_to_name(42)),  # Snare on beat 2
    (0.75, pretty_midi.note_number_to_name(36)),  # Kick on beat 3
    (1.125, pretty_midi.note_number_to_name(42)),  # Snare on beat 4
    (0, pretty_midi.note_number_to_name(49)),  # Hihat on beat 1
    (0.25, pretty_midi.note_number_to_name(49)),  # Hihat on beat 1.5
    (0.5, pretty_midi.note_number_to_name(49)),  # Hihat on beat 2
    (0.75, pretty_midi.note_number_to_name(49)),  # Hihat on beat 2.5
    (1.0, pretty_midi.note_number_to_name(49)),  # Hihat on beat 3
    (1.25, pretty_midi.note_number_to_name(49)),  # Hihat on beat 3.5
    (1.5, pretty_midi.note_number_to_name(49)),  # Hihat on beat 4
]

# Bar 2: Drums fill with syncopation
bar2_drums = [
    (0, pretty_midi.note_number_to_name(36)),  # Kick on beat 1
    (0.125, pretty_midi.note_number_to_name(49)),  # Hihat on 1.25
    (0.5, pretty_midi.note_number_to_name(42)),  # Snare on beat 2
    (0.75, pretty_midi.note_number_to_name(36)),  # Kick on beat 3
    (1.0, pretty_midi.note_number_to_name(49)),  # Hihat on 3.5
    (1.25, pretty_midi.note_number_to_name(42)),  # Snare on beat 4
    (1.5, pretty_midi.note_number_to_name(49)),  # Hihat on 4
]

# Bar 3: More syncopation, tensions
bar3_drums = [
    (0.25, pretty_midi.note_number_to_name(49)),  # Hihat on 1.25
    (0.5, pretty_midi.note_number_to_name(42)),  # Snare on beat 2
    (0.75, pretty_midi.note_number_to_name(36)),  # Kick on beat 3
    (1.0, pretty_midi.note_number_to_name(49)),  # Hihat on 3.5
    (1.25, pretty_midi.note_number_to_name(42)),  # Snare on beat 4
    (1.5, pretty_midi.note_number_to_name(49)),  # Hihat on 4
]

# Bar 4: Build to resolution
bar4_drums = [
    (0, pretty_midi.note_number_to_name(36)),  # Kick on beat 1
    (0.5, pretty_midi.note_number_to_name(42)),  # Snare on beat 2
    (1.0, pretty_midi.note_number_to_name(36)),  # Kick on beat 3
    (1.5, pretty_midi.note_number_to_name(42)),  # Snare on beat 4
    (0, pretty_midi.note_number_to_name(49)),  # Hihat on every eighth
    (0.25, pretty_midi.note_number_to_name(49)),
    (0.5, pretty_midi.note_number_to_name(49)),
    (0.75, pretty_midi.note_number_to_name(49)),
    (1.0, pretty_midi.note_number_to_name(49)),
    (1.25, pretty_midi.note_number_to_name(49)),
    (1.5, pretty_midi.note_number_to_name(49)),
]

# Add all drum notes
for note in bar1_drums:
    drum_instrument.notes.append(pretty_midi.Note(velocity=np.random.randint(60, 100), pitch=note[1], start=0.0 + note[0], end=0.0 + note[0] + 0.05))
for note in bar2_drums:
    drum_instrument.notes.append(pretty_midi.Note(velocity=np.random.randint(60, 100), pitch=note[1], start=bar_time + note[0], end=bar_time + note[0] + 0.05))
for note in bar3_drums:
    drum_instrument.notes.append(pretty_midi.Note(velocity=np.random.randint(60, 100), pitch=note[1], start=2*bar_time + note[0], end=2*bar_time + note[0] + 0.05))
for note in bar4_drums:
    drum_instrument.notes.append(pretty_midi.Note(velocity=np.random.randint(60, 100), pitch=note[1], start=3*bar_time + note[0], end=3*bar_time + note[0] + 0.05))

# ---------------------
# PIANO: Diane (7th chords, comp on 2 and 4)
# ---------------------
# Key: F major
chords = {
    # Bar 1: F7 (F, A, C, E)
    0: [59, 64, 61, 65],
    # Bar 2: G7 (G, B, D, F)
    1: [60, 65, 62, 61],
    # Bar 3: C7 (C, E, G, B)
    2: [61, 65, 62, 67],
    # Bar 4: F7 (F, A, C, E)
    3: [59, 64, 61, 65],
}

# Add piano notes
for i, chord in enumerate(chords.values()):
    start = i * bar_time
    for note in chord:
        # Play on 2 and 4
        if i == 0:
            # Bar 1: comp on 2 and 4
            piano_instrument.notes.append(pretty_midi.Note(velocity=np.random.randint(80, 100), pitch=note, start=start + 0.75, end=start + 0.75 + 0.15))
            piano_instrument.notes.append(pretty_midi.Note(velocity=np.random.randint(80, 100), pitch=note, start=start + 1.5, end=start + 1.5 + 0.15))
        elif i == 1:
            piano_instrument.notes.append(pretty_midi.Note(velocity=np.random.randint(80, 100), pitch=note, start=start + 0.75, end=start + 0.75 + 0.15))
            piano_instrument.notes.append(pretty_midi.Note(velocity=np.random.randint(80, 100), pitch=note, start=start + 1.5, end=start + 1.5 + 0.15))
        elif i == 2:
            piano_instrument.notes.append(pretty_midi.Note(velocity=np.random.randint(80, 100), pitch=note, start=start + 0.75, end=start + 0.75 + 0.15))
            piano_instrument.notes.append(pretty_midi.Note(velocity=np.random.randint(80, 100), pitch=note, start=start + 1.5, end=start + 1.5 + 0.15))
        elif i == 3:
            piano_instrument.notes.append(pretty_midi.Note(velocity=np.random.randint(80, 100), pitch=note, start=start + 0.75, end=start + 0.75 + 0.15))
            piano_instrument.notes.append(pretty_midi.Note(velocity=np.random.randint(80, 100), pitch=note, start=start + 1.5, end=start + 1.5 + 0.15))

# ---------------------
# BASS: Marcus (walking line, chromatic approaches)
# ---------------------
# F major scale: F, G, A, Bb, B, C, D, E
# Walking line in F (key: F major)
bass_line = [
    # Bar 1: F -> G -> A -> Bb
    (0.0, 59),  # F
    (0.375, 60),  # G
    (0.75, 61),  # A
    (1.125, 62),  # Bb (chromatic approach)
    # Bar 2: B -> C -> D -> E
    (1.5, 63),  # B
    (1.875, 61),  # C
    (2.25, 62),  # D
    (2.625, 65),  # E (chromatic approach)
    # Bar 3: F -> G -> A -> Bb
    (3.0, 59),  # F
    (3.375, 60),  # G
    (3.75, 61),  # A
    (4.125, 62),  # Bb (chromatic approach)
    # Bar 4: B -> C -> D -> F (resolution)
    (4.5, 63),  # B
    (4.875, 61),  # C
    (5.25, 62),  # D
    (5.625, 59),  # F
]

for time, pitch in bass_line:
    bass_instrument.notes.append(pretty_midi.Note(velocity=np.random.randint(60, 90), pitch=pitch, start=time, end=time + 0.1))

# ---------------------
# SAX: You (melody - simple, haunting, space and silence)
# ---------------------
# Motif: F -> A -> C -> Bb (F7)
# Bar 2: Repeat motif, shifted
# Bar 3: Repeat motif, variation
# Bar 4: Resolve to F

sax_notes = [
    # Bar 1: C (start) -> Bb (end)
    (0.0, 61),  # C
    (0.5, 62),  # Bb

    # Bar 2: F -> A -> C -> Bb (motif)
    (1.5, 59),  # F
    (1.75, 64),  # A
    (2.0, 61),  # C
    (2.25, 62),  # Bb

    # Bar 3: F -> A -> C -> Bb (variation)
    (3.0, 59),  # F
    (3.25, 64),  # A
    (3.5, 61),  # C
    (3.75, 62),  # Bb

    # Bar 4: F -> A -> C -> Bb (resolution)
    (4.5, 59),  # F
    (4.75, 64),  # A
    (5.0, 61),  # C
    (5.25, 62),  # Bb
]

for time, pitch in sax_notes:
    sax_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.1))

# Add instruments to the PrettyMIDI object
pm.instruments.append(drum_instrument)
pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(sax_instrument)

# Write to MIDI file
pm.write("The_Cellar_Moment.mid")
print("MIDI file saved as 'The_Cellar_Moment.mid'")
