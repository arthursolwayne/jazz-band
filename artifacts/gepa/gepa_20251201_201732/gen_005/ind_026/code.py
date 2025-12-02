
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
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (Dm7) - D, F, A, C
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.5 + 0.375),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=1.875 + 0.375), # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.25 + 0.375), # A2
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=2.625 + 0.375), # G2

    # Bar 3 (G7) - G, B, D, F
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=2.625 + 0.375),  # G2
    pretty_midi.Note(velocity=80, pitch=45, start=2.625 + 0.75, end=2.625 + 0.75 + 0.375), # B2
    pretty_midi.Note(velocity=80, pitch=47, start=2.625 + 1.125, end=2.625 + 1.125 + 0.375), # D3
    pretty_midi.Note(velocity=80, pitch=44, start=2.625 + 1.5, end=2.625 + 1.5 + 0.375), # F3

    # Bar 4 (Cm7) - C, Eb, G, Bb
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.0 + 0.375),  # C3
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.375 + 0.375), # Eb3
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=3.75 + 0.375), # G3
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.125 + 0.375), # Bb3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.375),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.375),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.375),  # C4

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.625 + 0.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.625 + 0.375),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.625 + 0.375),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.625 + 0.375),  # F5

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.0 + 0.375),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + 0.375),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.0 + 0.375),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: First motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.375),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=1.875 + 0.375),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.25 + 0.375),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.625 + 0.375),  # D4

    # Bar 4: Return and resolve
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.5 + 0.375),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=4.875 + 0.375),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.25 + 0.375),  # A4
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=5.625 + 0.375),  # C4
]
sax.notes.extend(sax_notes)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
