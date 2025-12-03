
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
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat_1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)

    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (38), C (43), chromatic approach on D (39)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=39, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),
    
    # Bar 3: Bb (41), F (38), chromatic approach on E (40)
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),
    
    # Bar 4: D (40), A (45), chromatic approach on C (43)
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),
    
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),
    
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (60), Bb (62), D (65), rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625)
]
sax.notes.extend(sax_notes)

# Drums: Same pattern as Bar 1
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat_1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)

    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
