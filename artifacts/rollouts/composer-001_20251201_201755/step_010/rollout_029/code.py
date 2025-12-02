
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
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) -> C#2 (chromatic approach) -> G2 (fifth) -> F#2 (chromatic)
    pretty_midi.Note(velocity=110, pitch=38, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=37, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=43, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=42, start=1.875, end=2.0),

    # Bar 3: G2 (fifth) -> F#2 (chromatic) -> D2 (root) -> C#2 (chromatic)
    pretty_midi.Note(velocity=110, pitch=43, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=42, start=2.125, end=2.25),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=37, start=2.375, end=2.5),

    # Bar 4: D2 (root) -> C#2 (chromatic) -> G2 (fifth) -> F#2 (chromatic)
    pretty_midi.Note(velocity=110, pitch=38, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=37, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=43, start=2.75, end=2.875),
    pretty_midi.Note(velocity=110, pitch=42, start=2.875, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
# Bar 3: Gm7 (G-Bb-D-F)
# Bar 4: Cm7 (C-Eb-G-Bb)
for bar in range(2, 5):
    start = (bar - 2) * 1.5 + 1.5
    if bar == 2:
        # Dm7: D4, F4, A4, C4
        notes = [62, 65, 67, 60]
    elif bar == 3:
        # Gm7: G4, Bb4, D4, F4
        notes = [67, 69, 62, 65]
    elif bar == 4:
        # Cm7: C4, Eb4, G4, Bb4
        notes = [60, 64, 67, 69]
    for pitch in notes:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 1.5)
        piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D E F G A Bb C D
# Motif: D - F - G - F (Dm triad with a twist)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F4 again, delayed
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D4, resolution
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4 (1.5 - 6.0s) - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    for beat in range(4):
        time = (bar - 2) * 1.5 + 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
