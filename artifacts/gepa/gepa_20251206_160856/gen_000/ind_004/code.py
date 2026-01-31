
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
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F (F2, A2, C3, D3, F3, G3, A3, C4), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=78, start=1.875, end=2.25), # A2
    pretty_midi.Note(velocity=80, pitch=81, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=80, pitch=82, start=2.625, end=3.0),  # D3
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=77, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=80, pitch=78, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=80, pitch=81, start=4.125, end=4.5),  # C3
    pretty_midi.Note(velocity=80, pitch=81, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=80, pitch=83, start=4.875, end=5.25), # D#3
    pretty_midi.Note(velocity=80, pitch=84, start=5.25, end=5.625), # E3
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=6.0),  # C3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
chord2 = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=83, start=1.5, end=1.875),
]
piano.notes.extend(chord2)

# Bar 3: Gm7 (G, Bb, D, F)
chord3 = [
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),
]
piano.notes.extend(chord3)

# Bar 4: C7 (C, E, G, Bb)
chord4 = [
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=83, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),
]
piano.notes.extend(chord4)

# Sax: One short motif, make it sing
# Motif: F, G, A, Bb (F, G, A, Bb)
# Start it, leave it hanging. Come back and finish it.
motif = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=78, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=78, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),
]
sax.notes.extend(motif)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5 - 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
