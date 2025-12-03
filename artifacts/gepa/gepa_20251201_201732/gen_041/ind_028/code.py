
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
    # Hi-Hat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # C
]
sax.notes.extend(sax_notes)

# Bass: walking line (F, G, A, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: chord on bar 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0), # C
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0), # E
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # C
]
sax.notes.extend(sax_notes)

# Bass: walking line (Bb, C, D, E)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=47, start=4.125, end=4.5),  # E
]
bass.notes.extend(bass_notes)

# Piano: chord on bar 3
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=4.5), # F
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=4.5), # A
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5), # C
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5), # E
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Bass: walking line (F, G, A, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: chord on bar 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=6.0), # F
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=6.0), # A
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0), # C
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0), # E
]
piano.notes.extend(piano_notes)

# Drums for bar 3 and 4
for bar in range(2, 4):
    start_time = 1.5 * (bar + 1)
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.0),
    # Hi-Hat on every eighth
    for i in range(8):
        start = start_time + i * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
