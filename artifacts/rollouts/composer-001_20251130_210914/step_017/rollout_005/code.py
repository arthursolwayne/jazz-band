
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),# hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),# hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=44, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=45, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=2.75, end=3.0),  # F#
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=43, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=45, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=100, pitch=44, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=100, pitch=43, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=100, pitch=44, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=45, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=5.75, end=6.0),  # F#
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # C
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=110, pitch=66, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=110, pitch=66, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: continue with fill
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375),# hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),# kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.8125),# hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875), # hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75), # kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625),# hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.375),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.1875), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.375, end=4.5625),# kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.375, end=4.5625),# hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=5.125),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.75, end=4.9375), # hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.125, end=5.5),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=5.125, end=5.3125),# hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.875),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.5, end=5.6875), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.875, end=6.0),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.875, end=6.0),  # hihat on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
