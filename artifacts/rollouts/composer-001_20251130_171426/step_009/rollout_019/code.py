
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
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick_time = bar_start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    kick_time = bar_start + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare_time = bar_start + 0.375
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    snare_time = bar_start + 1.125
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat_time = bar_start + (i * 0.375)
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.5),  # G#
    pretty_midi.Note(velocity=90, pitch=53, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=90, pitch=51, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=90, pitch=52, start=3.5, end=3.75),  # G#
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=54, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=4.25, end=4.5),  # G#
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=51, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.5),  # G#
    pretty_midi.Note(velocity=90, pitch=53, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=90, pitch=52, start=5.75, end=6.0),  # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # Dm7 (F)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # Dm7 (A)
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.75),  # Dm7 (C)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # Dm7 (C#)
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),  # Dm7 (F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # Dm7 (A)
    pretty_midi.Note(velocity=90, pitch=70, start=2.0, end=2.25),  # Dm7 (C)
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),  # Dm7 (C#)
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.75),  # Dm7 (F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # Dm7 (A)
    pretty_midi.Note(velocity=90, pitch=70, start=2.5, end=2.75),  # Dm7 (C)
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # Dm7 (C#)
    # Bar 5 (3.0 - 3.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # Dm7 (F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # Dm7 (A)
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.25),  # Dm7 (C)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # Dm7 (C#)
    # Bar 6 (3.5 - 4.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # Dm7 (F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # Dm7 (A)
    pretty_midi.Note(velocity=90, pitch=70, start=3.5, end=3.75),  # Dm7 (C)
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # Dm7 (C#)
    # Bar 7 (4.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25),  # Dm7 (F)
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),  # Dm7 (A)
    pretty_midi.Note(velocity=90, pitch=70, start=4.0, end=4.25),  # Dm7 (C)
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),  # Dm7 (C#)
    # Bar 8 (4.5 - 5.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # Dm7 (F)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # Dm7 (A)
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.75),  # Dm7 (C)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # Dm7 (C#)
    # Bar 9 (5.0 - 5.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25),  # Dm7 (F)
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),  # Dm7 (A)
    pretty_midi.Note(velocity=90, pitch=70, start=5.0, end=5.25),  # Dm7 (C)
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.25),  # Dm7 (C#)
    # Bar 10 (5.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # Dm7 (F)
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),  # Dm7 (A)
    pretty_midi.Note(velocity=90, pitch=70, start=5.5, end=5.75),  # Dm7 (C)
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75),  # Dm7 (C#)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, Bb, F, D (as a triplet on beat 1), then F, D (on beat 2), then G, A, Bb, C (on beat 3)
# Keep the motif legato, sing it like a story.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6667),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.6667, end=1.8333),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.8333, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: continue the pattern for bars 2-4
for bar in range(2, 4):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick_time = bar_start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    kick_time = bar_start + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare_time = bar_start + 0.375
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    snare_time = bar_start + 1.125
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat_time = bar_start + (i * 0.375)
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
