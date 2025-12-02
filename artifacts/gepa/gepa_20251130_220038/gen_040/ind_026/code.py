
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus's walking line, chromatic approaches, no repeating notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25), # Gb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # F#
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.125), # C#
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: Diane's comping on 2 and 4, 7th chords
# F7 = F A C Eb
# Bb7 = Bb D F Ab
# G7 = G B D F
# C7 = C E G B
piano_notes = [
    # Bar 2 (1.5 - 2.25)
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=95, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=95, pitch=77, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=95, pitch=74, start=1.5, end=1.875),  # Eb
    # Bar 3 (2.25 - 3.0)
    pretty_midi.Note(velocity=95, pitch=79, start=2.625, end=2.875),  # Bb
    pretty_midi.Note(velocity=95, pitch=84, start=2.625, end=2.875),  # D
    pretty_midi.Note(velocity=95, pitch=77, start=2.625, end=2.875),  # F
    pretty_midi.Note(velocity=95, pitch=81, start=2.625, end=2.875),  # Ab
    # Bar 4 (3.0 - 3.75)
    pretty_midi.Note(velocity=95, pitch=77, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=95, pitch=82, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=95, pitch=79, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=95, pitch=77, start=3.0, end=3.25),  # F
    # Bar 4 (4.5 - 5.25)
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=95, pitch=77, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=95, pitch=79, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=95, pitch=81, start=4.5, end=4.75),  # B
]
piano.notes.extend(piano_notes)

# Sax: Dante's melody
sax_notes = [
    # Bar 2 (1.5 - 1.875)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=77, start=1.75, end=1.875),  # C
    # Bar 3 (2.25 - 2.625)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=76, start=2.375, end=2.5),   # A
    pretty_midi.Note(velocity=100, pitch=77, start=2.5, end=2.625),   # C
    # Bar 4 (3.0 - 3.375)
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=81, start=3.125, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=3.25, end=3.375),  # Bb
    # Bar 4 (4.5 - 4.875)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.625, end=4.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=4.875),  # A
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)
    drums.notes.extend([kick1, hihat1, snare2, hihat2, kick3, hihat3, snare4, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
