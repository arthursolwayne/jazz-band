
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

# Kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.append(drum_kick_1)
drums.notes.append(drum_kick_2)

# Snare on 2 and 4
drum_snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875)
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0)
drums.notes.append(drum_snare_1)
drums.notes.append(drum_snare_2)

# Hihat on every eighth
for i in range(0, 4):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=i * 0.375, end=i * 0.375 + 0.125)
    drums.notes.append(hihat)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=2.375, end=2.5),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.875, end=3.0),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.125),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.5),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.875, end=4.0),  # D
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
# Dm7 = D - F - A - C
piano_notes = [
    # Bar 2 (1.5-2.0s) - comp on beat 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=80, pitch=59, start=1.75, end=1.875),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=1.875),  # C
    # Bar 3 (2.5-3.0s) - comp on beat 2
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=2.875),  # E
    pretty_midi.Note(velocity=80, pitch=59, start=2.75, end=2.875),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=2.875),  # C
    # Bar 4 (3.5-4.0s) - comp on beat 2
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=3.875),  # E
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=3.875),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=3.875),  # C
]
piano.notes.extend(piano_notes)

# Sax - melody in Dm, one short motif
# Motif: D - F - A - D (1.5-2.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D
]
sax.notes.extend(sax_notes)

# Repeat motif, but leave it hanging (2.0-2.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.125, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),  # D
]
sax.notes.extend(sax_notes)

# Return to motif and finish it (3.0-3.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
