
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
for bar in range(1):
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5, end=bar*1.5 + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + 0.75, end=bar*1.5 + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=bar*1.5 + 0.375, end=bar*1.5 + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=bar*1.5 + 1.125, end=bar*1.5 + 1.5)
    drums.notes.append(snare)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + i*0.375, end=bar*1.5 + i*0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0)
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales.
# Dm: D (38), F (41), A (45), C (48), G (43), Bb (46)
bass_notes = [
    # Bar 2 (Dm)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=1.75, end=2.0),  # F
    # Bar 3 (Dm)
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.5),  # A
    # Bar 4 (Dm)
    pretty_midi.Note(velocity=80, pitch=48, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=45, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=80, pitch=43, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=38, start=4.75, end=5.0)   # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=63, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=66, start=3.5, end=3.75)
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4 + 1):  # Bars 2, 3, 4
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(snare)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i*0.375, end=start + i*0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
