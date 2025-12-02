
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0), # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5), # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0), # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, 2nd beat (C7)
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # B
    # Bar 2, 4th beat (F7)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0), # B
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0), # C
    # Bar 3, 2nd beat (G7)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75), # D
    # Bar 3, 4th beat (C7)
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5), # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5), # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5), # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5), # B
    # Bar 4, 2nd beat (F7)
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25), # C
    # Bar 4, 4th beat (G7)
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0), # B
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0), # C
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0), # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0), # F
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5), # F
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0), # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
