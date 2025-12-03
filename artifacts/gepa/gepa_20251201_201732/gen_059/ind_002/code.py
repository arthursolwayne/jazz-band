
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
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 - Bb2), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25), # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=90, pitch=59, start=2.625, end=3.0),  # Bb2
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # Bb2 (fifth)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75), # C3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # D3
    pretty_midi.Note(velocity=90, pitch=66, start=4.125, end=4.5),  # Eb3
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # Eb3 (fifth)
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # F3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # G3
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),  # G3 (fifth)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # E
]
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625), # Ab
]
# Bar 4: C7 (C, E, G, Bb)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # Bb
]
# Bar 4: Resolving to Fmaj7 (F, A, C, E)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # E
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53) - Bb (57) - D (62) - F (53)
# Start on bar 2 (1.5s), end with a trailing note
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=110, pitch=57, start=1.625, end=1.75), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875), # D
    pretty_midi.Note(velocity=110, pitch=53, start=1.875, end=2.0),  # F (trailing)
    pretty_midi.Note(velocity=110, pitch=53, start=2.625, end=2.75), # F (return)
    pretty_midi.Note(velocity=110, pitch=57, start=2.75, end=2.875), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.125),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
