
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875),  # Fm root
    pretty_midi.Note(velocity=80, pitch=45, start=1.875, end=2.25),  # b9
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.625),  # 3
    pretty_midi.Note(velocity=80, pitch=47, start=2.625, end=3.0),  # #4
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # b9
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # root
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # b7
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),  # b6
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.875),  # b5
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),  # b6
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # b7
    pretty_midi.Note(velocity=80, pitch=44, start=5.625, end=6.0),  # root
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=95, pitch=44, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875),
    # Bar 3: Bbm7
    pretty_midi.Note(velocity=95, pitch=41, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=2.875),
    # Bar 4: Fm7 again
    pretty_midi.Note(velocity=95, pitch=44, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),
]
piano.notes.extend(piano_notes)

# Sax: Melody - Whisper at first, then a cry
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=85, pitch=53, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=85, pitch=51, start=1.75, end=2.0),  # E
    # Bar 3: Build and tension
    pretty_midi.Note(velocity=95, pitch=55, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=95, pitch=56, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=2.75, end=3.0),  # E
    # Bar 4: Return and resolve
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.625),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=3.625, end=3.875),  # E
    pretty_midi.Note(velocity=95, pitch=55, start=3.875, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=95, pitch=55, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.125),  # E
    pretty_midi.Note(velocity=85, pitch=53, start=5.125, end=5.5),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=5.5, end=5.875),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=5.875, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Continue kick, snare, hihat for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.875, end=start + 2.25)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_intro.mid")
