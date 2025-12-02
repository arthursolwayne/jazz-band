
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=41, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=40, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=41, start=2.75, end=3.0),  # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=39, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=40, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=38, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=39, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=40, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=4.25, end=4.5),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=41, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=40, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=5.75, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2 (1.5 - 3.0s)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=2.0),  # A (F7)
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # C
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=63, start=3.25, end=3.5),  # A (F7)
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # C
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=63, start=5.0, end=5.25),  # A (F7)
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, Eb (Fm scale) with a twist of chromaticism
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.6875, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.1875),  # Eb (chromatic descent)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.1875, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.6875),  # Eb
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=4.6875, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.1875),  # Eb
    # Resolution
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.6875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.6875, end=5.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.875, end=6.0),  # Eb
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick_start = start
    kick_end = kick_start + 0.375
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    drums.notes.append(kick)
    kick_start = start + 1.125
    kick_end = kick_start + 0.375
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    drums.notes.append(kick)

# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    snare_start = start + 0.75
    snare_end = snare_start + 0.125
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare)
    snare_start = start + 1.875
    snare_end = snare_start + 0.125
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end)
    drums.notes.append(snare)

# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        hihat_start = start + (i * 0.1875)
        hihat_end = hihat_start + 0.1875
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
