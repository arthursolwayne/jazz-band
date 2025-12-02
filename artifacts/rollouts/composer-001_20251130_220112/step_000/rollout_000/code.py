
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
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    (1.5, 50, 100),  # G
    (1.875, 49, 100),  # F#
    (2.25, 50, 100),  # G
    (2.625, 52, 100),  # A
    (3.0, 53, 100),  # A#
    (3.375, 52, 100),  # A
    (3.75, 50, 100),  # G
    (4.125, 48, 100),  # F
    (4.5, 50, 100),  # G
    (4.875, 51, 100),  # G#
    (5.25, 50, 100),  # G
    (5.625, 52, 100),  # A
]
for time, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 64, 100),  # C7: C E G B
    (1.875, 69, 100),  # E
    (1.875, 71, 100),  # G
    (1.875, 76, 100),  # B
    # Bar 3
    (3.375, 64, 100),  # C7
    (3.375, 69, 100),  # E
    (3.375, 71, 100),  # G
    (3.375, 76, 100),  # B
    # Bar 4
    (5.625, 64, 100),  # C7
    (5.625, 69, 100),  # E
    (5.625, 71, 100),  # G
    (5.625, 76, 100),  # B
]
for time, pitch, vel in piano_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Motif starts at bar 2
sax_notes = [
    (1.5, 65, 110),  # F#
    (1.625, 67, 110),  # A
    (1.75, 65, 110),  # F#
    (2.25, 65, 110),  # F#
    (2.375, 67, 110),  # A
    (2.5, 69, 110),  # B
    (3.0, 67, 110),  # A
    (3.125, 65, 110),  # F#
    (3.25, 64, 110),  # E
    (3.75, 65, 110),  # F#
    (3.875, 67, 110),  # A
    (4.0, 69, 110),  # B
    (4.5, 65, 110),  # F#
    (4.625, 67, 110),  # A
    (4.75, 69, 110),  # B
    (5.25, 67, 110),  # A
    (5.375, 65, 110),  # F#
    (5.5, 64, 110),  # E
]
for time, pitch, vel in sax_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: continue for bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
