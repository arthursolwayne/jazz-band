
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
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
for bar in range(2, 5):
    start = bar * 1.5
    # Roots and fifths with chromatic approaches
    if bar == 2:
        bass_notes = [pretty_midi.Note(velocity=100, pitch=43, start=start, end=start + 0.375),  # D3
                      pretty_midi.Note(velocity=100, pitch=41, start=start + 0.375, end=start + 0.75),  # B3
                      pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125),  # C#4
                      pretty_midi.Note(velocity=100, pitch=43, start=start + 1.125, end=start + 1.5)]  # D3
    elif bar == 3:
        bass_notes = [pretty_midi.Note(velocity=100, pitch=43, start=start, end=start + 0.375),  # D3
                      pretty_midi.Note(velocity=100, pitch=41, start=start + 0.375, end=start + 0.75),  # B3
                      pretty_midi.Note(velocity=100, pitch=40, start=start + 0.75, end=start + 1.125),  # A3
                      pretty_midi.Note(velocity=100, pitch=43, start=start + 1.125, end=start + 1.5)]  # D3
    else:  # bar == 4
        bass_notes = [pretty_midi.Note(velocity=100, pitch=43, start=start, end=start + 0.375),  # D3
                      pretty_midi.Note(velocity=100, pitch=41, start=start + 0.375, end=start + 0.75),  # B3
                      pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125),  # C#4
                      pretty_midi.Note(velocity=100, pitch=43, start=start + 1.125, end=start + 1.5)]  # D3
    bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bars 2-4: Dmaj7, G7, Cmaj7
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Dmaj7: D, F#, A, C#
        notes = [pretty_midi.Note(velocity=100, pitch=50, start=start, end=start + 0.75),  # D4
                 pretty_midi.Note(velocity=100, pitch=53, start=start, end=start + 0.75),  # F#4
                 pretty_midi.Note(velocity=100, pitch=55, start=start, end=start + 0.75),  # A4
                 pretty_midi.Note(velocity=100, pitch=57, start=start, end=start + 0.75)]  # C#5
    elif bar == 3:
        # G7: G, B, D, F
        notes = [pretty_midi.Note(velocity=100, pitch=55, start=start, end=start + 0.75),  # G4
                 pretty_midi.Note(velocity=100, pitch=58, start=start, end=start + 0.75),  # B4
                 pretty_midi.Note(velocity=100, pitch=60, start=start, end=start + 0.75),  # D5
                 pretty_midi.Note(velocity=100, pitch=57, start=start, end=start + 0.75)]  # F5
    else:  # bar == 4
        # Cmaj7: C, E, G, B
        notes = [pretty_midi.Note(velocity=100, pitch=52, start=start, end=start + 0.75),  # C4
                 pretty_midi.Note(velocity=100, pitch=55, start=start, end=start + 0.75),  # E4
                 pretty_midi.Note(velocity=100, pitch=57, start=start, end=start + 0.75),  # G4
                 pretty_midi.Note(velocity=100, pitch=59, start=start, end=start + 0.75)]  # B4
    piano.notes.extend(notes)

# Drums: continue on bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (50), E4 (52), F#4 (53), D5 (57) — two phrases with space in between
# First phrase on bar 2, second phrase on bar 4

# Bar 2: first phrase
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=52, start=1.75, end=2.0),   # E4
    pretty_midi.Note(velocity=110, pitch=53, start=2.0, end=2.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=57, start=2.25, end=2.5)   # D5
]
sax.notes.extend(sax_notes)

# Bar 4: second phrase (finish the motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=50, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=110, pitch=52, start=4.75, end=5.0),   # E4
    pretty_midi.Note(velocity=110, pitch=53, start=5.0, end=5.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=57, start=5.25, end=5.5)   # D5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
