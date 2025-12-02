
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=80, pitch=54, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=80, pitch=56, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: F7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # F
]
# Bar 3: F7 on beat 2
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # F
])
# Bar 4: F7 on beat 2
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # F
])
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: F, Bb, D, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_intro.mid")
