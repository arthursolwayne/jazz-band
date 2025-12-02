
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: D2-G2, walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),  # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # F2
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),  # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)    # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C5
]
# Bar 3: G7 (G B D F)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # F5
]
# Bar 4: Bm7 (B D F# A)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),  # F#5
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # A5
]
# Bar 4: Resolve with D7 again
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # F#4
    pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # C5
]
# Second D7 in bar 4
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # C5
]
# Final D7 in bar 4
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # F#4
    pretty_midi.Note(velocity=95, pitch=71, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # C5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_note1 = pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875)  # F4
sax_note2 = pretty_midi.Note(velocity=115, pitch=68, start=2.25, end=2.625)  # A4
sax_note3 = pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375)  # F4
sax_note4 = pretty_midi.Note(velocity=115, pitch=68, start=3.75, end=4.125)  # A4
sax_note5 = pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875)  # F4
sax_note6 = pretty_midi.Note(velocity=115, pitch=68, start=5.25, end=5.625)  # A4
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4, sax_note5, sax_note6])

midi.instruments.extend([sax, bass, piano, drums])
midi.write('the_intro.mid')
