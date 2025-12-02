
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),  # C2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.625),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # D2

    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # C2
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),  # D2

    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # C2
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=63, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # C5

    # Bar 3: G7
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # F5

    # Bar 4: Cm7
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Bb4

    # Bar 4: Resolve to Dm7
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - A4 - C5 (Dm7 arpeggio), 1st bar, then leave it hanging on the last note
# Return in bar 4 to resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=63, start=1.6875, end=1.875),  # F4

    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.6875),  # A4
    pretty_midi.Note(velocity=110, pitch=70, start=4.6875, end=4.875),  # C5
]
sax.notes.extend(sax_notes)

# Drums in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat
    for i in range(8):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend([n for n in drums.notes if n not in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
