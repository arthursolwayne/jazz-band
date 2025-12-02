
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
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38), F#2 (41), G2 (43), A2 (45)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=41, start=1.5 + 0.375, end=1.5 + 0.75),
    pretty_midi.Note(velocity=90, pitch=43, start=1.5 + 0.75, end=1.5 + 1.125),
    pretty_midi.Note(velocity=90, pitch=45, start=1.5 + 1.125, end=1.5 + 1.5),
    # Bar 3: A2 (45), C#3 (48), D3 (50), E3 (52)
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.0 + 0.375),
    pretty_midi.Note(velocity=90, pitch=48, start=3.0 + 0.375, end=3.0 + 0.75),
    pretty_midi.Note(velocity=90, pitch=50, start=3.0 + 0.75, end=3.0 + 1.125),
    pretty_midi.Note(velocity=90, pitch=52, start=3.0 + 1.125, end=3.0 + 1.5),
    # Bar 4: E3 (52), G3 (55), A3 (57), B3 (59)
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=55, start=4.5 + 0.375, end=4.5 + 0.75),
    pretty_midi.Note(velocity=90, pitch=57, start=4.5 + 0.75, end=4.5 + 1.125),
    pretty_midi.Note(velocity=90, pitch=59, start=4.5 + 1.125, end=4.5 + 1.5)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.5 + 0.75),  # D3
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.5 + 0.75),  # F#3
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.5 + 0.75),  # A3
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.5 + 0.75),  # C#4
    # Bar 3: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.0 + 0.75),  # G3
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.0 + 0.75),  # B3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.75),  # D4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.0 + 0.75),  # F#4
    # Bar 4: A7 (A, C#, E, G#)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.5 + 0.75),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.75),  # C#5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.5 + 0.75),  # E5
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.5 + 0.75)   # G#5
]
piano.notes.extend(piano_notes)

# Drums continue for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D3 (50), F#3 (53), A3 (57), D4 (62) with space between
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=110, pitch=53, start=1.5 + 0.75, end=1.5 + 0.75 + 0.375),
    pretty_midi.Note(velocity=110, pitch=57, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375),
    pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
