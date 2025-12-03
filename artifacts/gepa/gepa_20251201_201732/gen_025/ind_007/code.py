
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for bar in range(1):
    time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.375, end=time + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=time + 1.125, end=time + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # G2
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.25), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # G2

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5

    # Bar 3: Bm7 (B D F# A)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A4

    # Bar 4: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875)   # F4
]
piano.notes.extend(piano_notes)

# Drums: Full kit
for bar in range(2, 5):
    time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.375, end=time + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=time + 1.125, end=time + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62) -> F#4 (67) -> D4 (62) -> Bb4 (66)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875), # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.4375),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=2.4375, end=2.625)  # Bb4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
