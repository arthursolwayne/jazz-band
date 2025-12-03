
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # F#2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # A2
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75), # F#2
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625), # F#2
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # A2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
]

# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F5
])

# Bar 4: C7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
])

# Bar 4: Bm7 (B D F# A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # F#5
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # A5
])

# Bar 4: D7 (D F# A C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # C5
])

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - A4 (from Bar 2), then leave it hanging
# Resumption: D4 - F#4 - D4 (Bar 4)

sax_notes = [
    # Bar 2: D4 - F#4 - A4
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),
    # Bar 3: Leave it hanging (no notes)
    # Bar 4: D4 - F#4 - D4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drum_notes(start_time):
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 1.125))
    # Hihat on 1 & 2 & 3 & 4
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.375))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 2.25))
    # Hihat
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.5 + i * 0.375, end=start_time + 1.5 + i * 0.375 + 0.375))
    # Kick on 1 (next bar)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time + 2.625, end=start_time + 2.625 + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 3.0, end=start_time + 3.375))
    # Hihat
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_time + 3.0 + i * 0.375, end=start_time + 3.0 + i * 0.375 + 0.375))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time + 3.75, end=start_time + 4.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 4.5, end=start_time + 4.875))
    # Hihat
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_time + 4.5 + i * 0.375, end=start_time + 4.5 + i * 0.375 + 0.375))

add_drum_notes(1.5)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
