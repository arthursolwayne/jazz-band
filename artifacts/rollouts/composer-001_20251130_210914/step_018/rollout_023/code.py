
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
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F, Eb, D, C, Bb, A, G, F)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# Fm7 on 2nd beat of bar 2 (1.875 - 2.25)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # Ab
    # Fm7 on 2nd beat of bar 3 (3.375 - 3.75)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # Ab
    # Fm7 on 2nd beat of bar 4 (4.875 - 5.25)
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # Ab
]
piano.notes.extend(piano_notes)

# Dante: Motif in Fm
# Start on F (64), then Eb (60), then Bb (55), then resolve to D (59)
# Play the first three notes, leave it hanging on D
# Then come back and resolve to C (57) on beat 3
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=110, pitch=60, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=110, pitch=55, start=1.75, end=1.875), # Bb
    pretty_midi.Note(velocity=110, pitch=59, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=110, pitch=59, start=2.625, end=2.75), # D (return)
    pretty_midi.Note(velocity=110, pitch=57, start=2.75, end=3.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    start_time = 1.5 + bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    drums.notes.extend([kick1, kick2])

# Snare on 2 and 4
for bar in range(2, 4):
    start_time = 1.5 + bar * 1.5
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    drums.notes.extend([snare1, snare2])

# Hihat on every eighth
for bar in range(2, 4):
    start_time = 1.5 + bar * 1.5
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start_time + i * 0.1875, end=start_time + (i + 1) * 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
