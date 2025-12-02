
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice. He's the anchor.
# F minor walking bass line
bass_notes = [
    (1.5, 65), # F
    (1.875, 64), # E
    (2.25, 66), # F#
    (2.625, 67), # G
    (3.0, 65), # F
    (3.375, 64), # E
    (3.75, 66), # F#
    (4.125, 67), # G
    (4.5, 65), # F
    (4.875, 64), # E
    (5.25, 66), # F#
    (5.625, 67), # G
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
# F7, Bb7, E7, A7, F7, Bb7, E7, A7
piano_notes = [
    # Bar 2
    (1.5, 64), (1.5, 69), (1.5, 71), (1.5, 76), # F7
    # Bar 3
    (3.0, 62), (3.0, 67), (3.0, 69), (3.0, 74), # Bb7
    # Bar 4
    (4.5, 65), (4.5, 70), (4.5, 72), (4.5, 77), # E7
    (6.0, 64), (6.0, 69), (6.0, 71), (6.0, 76), # A7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# You: This is your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, D (Fm7)
# First phrase: F, Ab, Bb, D (start at 1.5)
# Then silence, then repeat with a twist: F, Bb, C, D
sax_notes = [
    (1.5, 87), # F
    (1.625, 84), # Ab
    (1.75, 82), # Bb
    (1.875, 86), # D
    (2.25, 87), # F
    (2.375, 82), # Bb
    (2.5, 84), # C
    (2.625, 86), # D
    (3.0, 87), # F
    (3.125, 84), # Ab
    (3.25, 82), # Bb
    (3.375, 86), # D
    (3.75, 87), # F
    (3.875, 82), # Bb
    (4.0, 84), # C
    (4.125, 86), # D
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: Continue through bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dantes_intro.mid")
