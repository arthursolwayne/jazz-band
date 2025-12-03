
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Marcus - walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # C2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4

    # Bar 3: Bbm7 (Bb, Db, F, G)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # G3
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Ab3
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb3

    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # D3
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Eb3
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # G3
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb3
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - motif in Fm
# Motif: F, Ab, C, Eb (Fm chord), then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.6875),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=1.6875, end=1.875), # Ab4
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.0625), # C4
    pretty_midi.Note(velocity=110, pitch=65, start=2.0625, end=2.25), # Eb4
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.4375),  # F4 (return)
    pretty_midi.Note(velocity=110, pitch=68, start=2.4375, end=2.625), # Ab4
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=2.8125), # C4
    pretty_midi.Note(velocity=110, pitch=65, start=2.8125, end=3.0),  # Eb4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start+0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start+1.125, end=start+1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start+0.75, end=start+1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=start+1.875, end=start+2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start+0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start+0.375, end=start+0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start+0.75, end=start+1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start+1.125, end=start+1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=start+1.5, end=start+1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=start+1.875, end=start+2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=start+2.25, end=start+2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=start+2.625, end=start+3.0)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
