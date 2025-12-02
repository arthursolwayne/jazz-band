
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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

# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # F2
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),  # G2
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano (Diane) - Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # C4
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F4
])
# Bar 4: C7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
])
# Bar 4: resolve to D7 (repeat last bar with D7)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # C4
])
piano.notes.extend(piano_notes)

# Saxophone (Dante) - One short motif, make it sing
# Motif: D4 - G4 - B4 - D5 (hanging on D5)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),   # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75), # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125), # D5
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25), # D5
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625), # D5
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),  # D5
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Bar 1: 1.5 - 1.875 (Kick), 2.25 - 2.625 (Kick)
    # Snare on 2 and 4 (bar_start + 0.75 and bar_start + 1.5)
    # Hihat on every eighth
    for i in [0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]:
        if i == 0 or i == 0.75 or i == 1.5 or i == 2.25:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + i, end=bar_start + i + 0.375))
        elif i == 0.75 or i == 1.5 or i == 2.25:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + i, end=bar_start + i + 0.375))
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i, end=bar_start + i + 0.375))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
