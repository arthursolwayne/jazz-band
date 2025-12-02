
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
drum_notes = [
    (0.0, 36, 100),   # Kick on 1
    (0.75, 42, 100),  # Hihat on 2
    (1.5, 38, 100),   # Snare on 3
    (2.25, 42, 100),  # Hihat on 4
    (3.0, 36, 100),   # Kick on 1
    (3.75, 42, 100),  # Hihat on 2
    (4.5, 38, 100),   # Snare on 3
    (5.25, 42, 100),  # Hihat on 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line - walking line with chromatic approaches
bass_notes = [
    (1.5, 64, 100),   # F
    (1.875, 65, 100),  # F#
    (2.25, 63, 100),  # E
    (2.625, 64, 100),  # F
    (3.0, 65, 100),   # F#
    (3.375, 66, 100),  # G
    (3.75, 64, 100),  # F
    (4.125, 62, 100),  # E
    (4.5, 64, 100),   # F
    (4.875, 65, 100),  # F#
    (5.25, 63, 100),  # E
    (5.625, 64, 100),  # F
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Piano - comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2
    (1.875, 64, 100),  # F7
    (1.875, 71, 100),
    (2.625, 64, 100),
    (2.625, 71, 100),
    # Bar 3
    (3.375, 64, 100),  # F7
    (3.375, 71, 100),
    (4.125, 64, 100),
    (4.125, 71, 100),
    # Bar 4
    (4.875, 64, 100),  # F7
    (4.875, 71, 100),
    (5.625, 64, 100),
    (5.625, 71, 100),
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Sax - short motif, one phrase, leave it hanging
sax_notes = [
    (1.5, 72, 100),  # G
    (1.75, 76, 100),  # Bb
    (2.0, 72, 100),  # G
    (2.25, 77, 100),  # B
    (2.5, 74, 100),  # A
    (2.75, 76, 100),  # Bb
    (3.0, 72, 100),  # G
    (3.25, 77, 100),  # B
    (3.5, 74, 100),  # A
    (3.75, 72, 100),  # G
    (4.0, 76, 100),  # Bb
    (4.25, 77, 100),  # B
    (4.5, 74, 100),  # A
    (4.75, 72, 100),  # G
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_intro.mid')
