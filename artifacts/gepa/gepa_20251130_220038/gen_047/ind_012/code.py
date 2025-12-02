
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G7
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.875),  # F
    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A7
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),  # G
    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G7
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # F
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.5, end=start + 1.875)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 2.25, end=start + 2.625)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5)
    drums.notes.extend([kick1, snare2, kick3, snare4, hihat])

# Sax: Whisper at first, then cry (melody)
sax_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # A
    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # A
    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
