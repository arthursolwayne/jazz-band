
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (F, Ab, D, C), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.6875),   # F2 (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.6875, end=1.875), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.0625), # C3 (fifth)
    pretty_midi.Note(velocity=90, pitch=49, start=2.0625, end=2.25),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.4375),  # Ab2 (root)
    pretty_midi.Note(velocity=90, pitch=45, start=2.4375, end=2.625), # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=2.8125), # D3 (fifth)
    pretty_midi.Note(velocity=90, pitch=54, start=2.8125, end=3.0),   # C#2 (chromatic approach)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.1875),   # C3 (root)
    pretty_midi.Note(velocity=90, pitch=50, start=3.1875, end=3.375), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.5625), # F3 (fifth)
    pretty_midi.Note(velocity=90, pitch=58, start=3.5625, end=3.75),  # Eb3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=56, start=3.75, end=3.9375),  # D3 (root)
    pretty_midi.Note(velocity=90, pitch=54, start=3.9375, end=4.125), # C#3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.3125), # A3 (fifth)
    pretty_midi.Note(velocity=90, pitch=63, start=4.3125, end=4.5),   # G#3 (chromatic approach)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.6875),   # C3 (root)
    pretty_midi.Note(velocity=90, pitch=50, start=4.6875, end=4.875), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=59, start=4.875, end=5.0625), # F3 (fifth)
    pretty_midi.Note(velocity=90, pitch=58, start=5.0625, end=5.25),  # Eb3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=56, start=5.25, end=5.4375),  # D3 (root)
    pretty_midi.Note(velocity=90, pitch=54, start=5.4375, end=5.625), # C#3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=5.8125), # A3 (fifth)
    pretty_midi.Note(velocity=90, pitch=63, start=5.8125, end=6.0),   # G#3 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=90, pitch=61, start=1.5, end=1.75),  # Ab4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # C5
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # D5

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25),  # F5
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.25),  # Ab4

    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # F#5
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75),  # A5
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # C5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Motif: F4 - Ab4 - C5 - F5 (4 notes), played on beat 1 of bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=1.6875, end=1.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625), # C5
    pretty_midi.Note(velocity=100, pitch=72, start=2.0625, end=2.25),  # F5
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.6875),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=4.6875, end=4.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0625), # C5
    pretty_midi.Note(velocity=100, pitch=72, start=5.0625, end=5.25),  # F5
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + i * 0.1875, end=start_time + (i + 1) * 0.1875)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
