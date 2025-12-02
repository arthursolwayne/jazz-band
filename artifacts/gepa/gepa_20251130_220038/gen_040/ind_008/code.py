
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Snare on 2 and 4, hihat on every 8th, kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Hihat on every 8th note
for i in range(0, 4):
    pretty_midi.Note(velocity=100, pitch=42, start=i * 0.375, end=i * 0.375 + 0.1875).notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # F7: F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Your melody - short motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: continue to fill the bar with kick on 1 and 3, snare on 2 and 4
for i in range(2, 4):
    kick_start = i * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375).notes.append(note)
    snare_start = kick_start + 0.75
    pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375).notes.append(note)
    for j in range(0, 4):
        hihat_start = kick_start + j * 0.375
        pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.1875).notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
