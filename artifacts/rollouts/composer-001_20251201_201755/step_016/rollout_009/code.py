
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches (D2-G2, MIDI 38-43)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # D2# chromatic approach
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25), # D2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # D2#
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0), # F2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125), # G2#
    pretty_midi.Note(velocity=80, pitch=47, start=4.125, end=4.5),  # G2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25), # D2#
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0),  # D2#
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # C#5

    # Bar 3: D7 (D-F#-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C5

    # Bar 4: Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Motif: D4 - F#4 - G4 - D4
# Bar 2 (1.5 - 3.0s)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),   # F#4
    pretty_midi.Note(velocity=110, pitch=68, start=2.0, end=2.25),  # G4
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D4 (return)
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),   # F#4
    pretty_midi.Note(velocity=110, pitch=68, start=4.25, end=4.5),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D4
]
sax.notes.extend(sax_notes)

# Drums continue with same pattern for bars 2-4
# Bar 2 (1.5 - 3.0s)
for i in range(4):
    drum_notes.append(
        pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i*1.5, end=1.5 + i*1.5 + 0.375)
    )
    drum_notes.append(
        pretty_midi.Note(velocity=110, pitch=38, start=1.5 + i*1.5 + 0.75, end=1.5 + i*1.5 + 0.875)
    )
    for j in range(8):
        drum_notes.append(
            pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*1.5 + j*0.1875, end=1.5 + i*1.5 + j*0.1875 + 0.1875)
        )

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
