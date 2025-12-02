
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
    hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Add to drums
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

# Bars 2-4 (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Fm7 (F, C, Ab, D)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=58, start=1.875, end=2.25), # Ab (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # G (fifth)
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # Bb (chromatic approach)
]
# Bar 3: Bb7 (Bb, F, D, Ab)
bass_notes += [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb (root)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # D (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125), # C (fifth)
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # Eb (chromatic approach)
]
# Bar 4: Eb7 (Eb, Bb, G, D)
bass_notes += [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb (root)
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # G (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625), # F (fifth)
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # Ab (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Ab
]
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53) - Ab (58) - F (53) - G (57) (Bar 2)
#        C (57) - D (60) - C (57) - D (60) (Bar 4)
# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=58, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=53, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=57, start=2.625, end=3.0),
]
# Bar 4
sax_notes += [
    pretty_midi.Note(velocity=110, pitch=57, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=57, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 2 & 3
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat_1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Add to drums
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
