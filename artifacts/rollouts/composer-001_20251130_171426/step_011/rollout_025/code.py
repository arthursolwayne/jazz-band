
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=45, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0), # D
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=80, pitch=39, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5), # F
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875), # F#
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0), # C
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # E7 (Fm7)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=90, pitch=44, start=1.875, end=2.25), # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125), # Bb7 (Fm7)
    pretty_midi.Note(velocity=90, pitch=39, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.125), # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0), # Bb7 (Fm7)
    pretty_midi.Note(velocity=90, pitch=39, start=5.625, end=6.0), # Ab
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0), # E
    pretty_midi.Note(velocity=90, pitch=44, start=5.625, end=6.0), # F
]
piano.notes.extend(piano_notes)

# Saxophone (Dante) - motif, start it, leave it hanging, come back and finish it
# Motif: F (G#) - E - D - C (melody)
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=100, pitch=46, start=1.625, end=1.75), # G#
    pretty_midi.Note(velocity=100, pitch=43, start=1.75, end=1.875), # E
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0), # D
    # Bar 3: leave it hanging
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.125), # C
    pretty_midi.Note(velocity=100, pitch=43, start=3.125, end=3.25), # E
    pretty_midi.Note(velocity=100, pitch=42, start=3.25, end=3.375), # D
    # Bar 4: come back and finish it
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.625), # F
    pretty_midi.Note(velocity=100, pitch=46, start=4.625, end=4.75), # G#
    pretty_midi.Note(velocity=100, pitch=43, start=4.75, end=4.875), # E
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0), # D
    pretty_midi.Note(velocity=100, pitch=41, start=5.0, end=5.125), # C
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
