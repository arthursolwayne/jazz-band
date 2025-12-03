
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm
bass_notes = [
    # Bar 2: Fm - Root (F2), chromatic approach (E2), root (F2), 5th (C2)
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=76, start=2.125, end=2.5),
    pretty_midi.Note(velocity=90, pitch=81, start=2.5, end=2.875),
    # Bar 3: Bbm - Root (Bb2), chromatic approach (A2), root (Bb2), 5th (F2)
    pretty_midi.Note(velocity=90, pitch=70, start=2.875, end=3.25),
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=70, start=3.5, end=3.875),
    pretty_midi.Note(velocity=90, pitch=76, start=3.875, end=4.25),
    # Bar 4: Ebm - Root (Eb2), chromatic approach (D2), root (Eb2), 5th (Bb2)
    pretty_midi.Note(velocity=90, pitch=68, start=4.25, end=4.625),
    pretty_midi.Note(velocity=90, pitch=67, start=4.625, end=4.875),
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last chord
# Bar 2: Fm7 (F, Ab, C, Eb) - Open voicing
# Bar 3: Bbm7 (Bb, Db, F, Ab) - Open voicing
# Bar 4: Ebm7 (Eb, Gb, Bb, Db) - Open voicing
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),
    # Bar 3: Bbm7
    pretty_midi.Note(velocity=100, pitch=70, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),
    # Bar 4: Ebm7
    pretty_midi.Note(velocity=100, pitch=68, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=70, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=4.0),
]
piano_notes.extend([
    # Comp on 2 and 4 (Bar 2)
    pretty_midi.Note(velocity=80, pitch=76, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=71, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=81, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.125),
    # Comp on 2 and 4 (Bar 4)
    pretty_midi.Note(velocity=80, pitch=68, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=64, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=70, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=66, start=4.0, end=4.125),
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start of motif (F, Ab, D)
    pretty_midi.Note(velocity=110, pitch=76, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=74, start=2.0, end=2.25),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=76, start=2.5, end=2.75),
    pretty_midi.Note(velocity=110, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.25),
    # Bar 4: Return and finish it (F, Ab, D, G)
    pretty_midi.Note(velocity=110, pitch=76, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=110, pitch=74, start=4.0, end=4.25),
    pretty_midi.Note(velocity=110, pitch=78, start=4.25, end=4.5),
]
sax.notes.extend(sax_notes)

# Drums: Continue with the same pattern for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    hihat = [
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        for i in range(4)
    ]
    # Add notes
    drums.notes.extend([kick1, kick2, snare1, snare2])
    drums.notes.extend(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
