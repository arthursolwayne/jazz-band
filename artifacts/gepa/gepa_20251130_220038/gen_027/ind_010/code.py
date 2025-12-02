
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
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on 2
    (1.25, 42, 100), # Hihat on &2
    (1.5, 36, 100),  # Kick on 3
    (1.75, 42, 100), # Hihat on &3
    (2.0, 38, 100),  # Snare on 4
    (2.25, 42, 100)  # Hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line, chromatic approaches)
bass_notes = [
    (1.5, 59, 100),  # D (Fm7)
    (1.75, 60, 100), # Eb (chromatic)
    (2.0, 57, 100),  # Bb (Fm7)
    (2.25, 58, 100), # B (chromatic)
    (2.5, 55, 100),  # F (Fm7)
    (2.75, 56, 100), # Gb (chromatic)
    (3.0, 60, 100),  # Eb (Fm7)
    (3.25, 59, 100), # D (chromatic),
    (3.5, 57, 100),  # Bb (Fm7)
    (3.75, 58, 100), # B (chromatic)
    (4.0, 55, 100),  # F (Fm7)
    (4.25, 56, 100), # Gb (chromatic)
    (4.5, 60, 100),  # Eb (Fm7)
    (4.75, 59, 100), # D (chromatic)
    (5.0, 57, 100),  # Bb (Fm7)
    (5.25, 58, 100), # B (chromatic)
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2: Fm7
    (1.75, 53, 100), # F
    (1.75, 60, 100), # Eb
    (1.75, 64, 100), # Ab
    (1.75, 67, 100), # C
    # Bar 3: Bb7
    (3.25, 55, 100), # Bb
    (3.25, 58, 100), # D
    (3.25, 62, 100), # F
    (3.25, 67, 100), # C
    # Bar 4: Fm7
    (4.75, 53, 100), # F
    (4.75, 60, 100), # Eb
    (4.75, 64, 100), # Ab
    (4.75, 67, 100), # C
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 100), # Hihat on &1
    (2.0, 38, 100),  # Snare on 2
    (2.25, 42, 100), # Hihat on &2
    (2.5, 36, 100),  # Kick on 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on 4
    (3.25, 42, 100), # Hihat on &4
    # Bar 3
    (3.5, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on &1
    (4.0, 38, 100),  # Snare on 2
    (4.25, 42, 100), # Hihat on &2
    (4.5, 36, 100),  # Kick on 3
    (4.75, 42, 100), # Hihat on &3
    (5.0, 38, 100),  # Snare on 4
    (5.25, 42, 100), # Hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Sax: Dante (melody, one short motif)
sax_notes = [
    # Bar 2
    (1.5, 62, 100),  # G (Fm7)
    (1.75, 65, 100), # Bb
    (2.0, 60, 100),  # Eb
    (2.25, 62, 100), # G
    # Bar 3
    (3.0, 60, 100),  # Eb
    (3.25, 62, 100), # G
    (3.5, 64, 100),  # B
    (3.75, 62, 100), # G
    # Bar 4
    (4.0, 62, 100),  # G
    (4.25, 67, 100), # C
    (4.5, 65, 100),  # Bb
    (4.75, 62, 100), # G
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
