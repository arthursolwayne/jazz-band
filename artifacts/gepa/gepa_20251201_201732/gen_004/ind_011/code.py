
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Ab (b3)
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # G (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # C (5th)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - short and singing
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),  # Ab
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # C (5th)
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75), # Bb (7th)
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # B (chromatic)
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # F (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # Ab (b3)
    pretty_midi.Note(velocity=90, pitch=39, start=5.25, end=5.625), # G (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # C (5th)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),  # Ab
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
