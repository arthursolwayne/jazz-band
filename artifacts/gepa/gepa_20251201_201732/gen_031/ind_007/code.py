
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
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) -> chromatic approach to G2 (43)
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.625),  # chromatic
    pretty_midi.Note(velocity=100, pitch=38, start=1.625, end=1.75),  # D2
    pretty_midi.Note(velocity=100, pitch=43, start=1.75, end=1.875),  # G2
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.0),  # chromatic

    # Bar 3: G2 (43) -> chromatic approach to C3 (48)
    pretty_midi.Note(velocity=100, pitch=44, start=2.0, end=2.125),  # chromatic
    pretty_midi.Note(velocity=100, pitch=43, start=2.125, end=2.25),  # G2
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.375),  # C3
    pretty_midi.Note(velocity=100, pitch=49, start=2.375, end=2.5),  # chromatic

    # Bar 4: C3 (48) -> chromatic approach to F3 (53)
    pretty_midi.Note(velocity=100, pitch=49, start=2.5, end=2.625),  # chromatic
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=2.75),  # C3
    pretty_midi.Note(velocity=100, pitch=53, start=2.75, end=2.875),  # F3
    pretty_midi.Note(velocity=100, pitch=54, start=2.875, end=3.0),  # chromatic
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F3
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75),  # A3
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # C4

    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=55, start=2.0, end=2.25),  # G3
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.25),  # Bb3
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F4

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=2.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=100, pitch=70, start=2.5, end=2.75),  # Bb4
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D3 (50), F3 (53), G3 (55) -> D3 (50) again (half note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.25),  # D3
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # F3
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),  # G3
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.75),  # D3
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
