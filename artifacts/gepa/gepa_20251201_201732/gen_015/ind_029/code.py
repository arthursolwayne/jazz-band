
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
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, kick2, snare, snare2, hihat, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:  # Dm
        bass_notes = [pretty_midi.Note(velocity=90, pitch=38, start=start, end=start + 0.375),  # D2
                      pretty_midi.Note(velocity=90, pitch=41, start=start + 0.375, end=start + 0.75),  # F2
                      pretty_midi.Note(velocity=90, pitch=43, start=start + 0.75, end=start + 1.125),  # A2
                      pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)]  # G2
    elif bar == 3:  # Gm
        bass_notes = [pretty_midi.Note(velocity=90, pitch=43, start=start, end=start + 0.375),  # G2
                      pretty_midi.Note(velocity=90, pitch=46, start=start + 0.375, end=start + 0.75),  # B2
                      pretty_midi.Note(velocity=90, pitch=48, start=start + 0.75, end=start + 1.125),  # D3
                      pretty_midi.Note(velocity=90, pitch=47, start=start + 1.125, end=start + 1.5)]  # C3
    elif bar == 4:  # Cm
        bass_notes = [pretty_midi.Note(velocity=90, pitch=40, start=start, end=start + 0.375),  # C2
                      pretty_midi.Note(velocity=90, pitch=43, start=start + 0.375, end=start + 0.75),  # E2
                      pretty_midi.Note(velocity=90, pitch=45, start=start + 0.75, end=start + 1.125),  # G2
                      pretty_midi.Note(velocity=90, pitch=44, start=start + 1.125, end=start + 1.5)]  # F2
    bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:  # Dm7
        piano_notes = [pretty_midi.Note(velocity=100, pitch=59, start=start, end=start + 0.75),  # D4
                       pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.75),  # F4
                       pretty_midi.Note(velocity=100, pitch=67, start=start, end=start + 0.75),  # A4
                       pretty_midi.Note(velocity=100, pitch=64, start=start, end=start + 0.75)]  # G4
    elif bar == 3:  # Gm7
        piano_notes = [pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.75),  # G4
                       pretty_midi.Note(velocity=100, pitch=65, start=start, end=start + 0.75),  # B4
                       pretty_midi.Note(velocity=100, pitch=70, start=start, end=start + 0.75),  # D5
                       pretty_midi.Note(velocity=100, pitch=67, start=start, end=start + 0.75)]  # C5
    elif bar == 4:  # Cm7
        piano_notes = [pretty_midi.Note(velocity=100, pitch=58, start=start, end=start + 0.75),  # C4
                       pretty_midi.Note(velocity=100, pitch=61, start=start, end=start + 0.75),  # E4
                       pretty_midi.Note(velocity=100, pitch=66, start=start, end=start + 0.75),  # G4
                       pretty_midi.Note(velocity=100, pitch=63, start=start, end=start + 0.75)]  # F4
    piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (E4, C4), E4 (F4, D4), C4 (D4, B3)
# Bar 2: D4 -> E4 -> C4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # E4
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.25),  # C4
    # Bar 3: E4 -> F4 -> D4 (leave hanging)
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # E4
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # D4
    # Bar 4: C4 -> D4 -> B3 (resolve)
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # D4
    pretty_midi.Note(velocity=110, pitch=59, start=5.0, end=5.25)   # B3
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, kick2, snare, snare2, hihat, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
