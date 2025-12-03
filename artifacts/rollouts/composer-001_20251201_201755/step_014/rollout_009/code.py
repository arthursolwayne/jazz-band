
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
bar_length = 1.5
for bar in range(1):
    start = bar * bar_length
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    hihat_notes = [
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    ]
    drums.notes.extend([kick1, kick3, snare2, snare4] + hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = []
for bar in range(2, 5):
    start = bar * bar_length
    # Fm root (F2) and fifths (C3)
    # Root on 1, 3, 4, 5
    # Fifth on 2, 6, 7
    # Chromatic approaches
    if bar == 2:
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=start, end=start + 0.375))  # F2
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=40, start=start + 0.375, end=start + 0.75))  # Ab2
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=start + 0.75, end=start + 1.125))  # F2
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=start + 1.125, end=start + 1.5))  # C3
    elif bar == 3:
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=start, end=start + 0.375))  # C3
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=41, start=start + 0.375, end=start + 0.75))  # Bb2
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=start + 0.75, end=start + 1.125))  # C3
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=44, start=start + 1.125, end=start + 1.5))  # Db3
    elif bar == 4:
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=44, start=start, end=start + 0.375))  # Db3
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75))  # B2
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=44, start=start + 0.75, end=start + 1.125))  # Db3
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=start + 1.125, end=start + 1.5))  # F2
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
for bar in range(2, 5):
    start = bar * bar_length
    if bar == 2:
        # Fm7 (F, Ab, C, Eb)
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=start, end=start + 0.75))  # F4
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=51, start=start, end=start + 0.75))  # Ab4
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=start, end=start + 0.75))  # C5
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=start, end=start + 0.75))  # Eb5
    elif bar == 3:
        # Bb7 (Bb, D, F, Ab)
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=start, end=start + 0.75))  # Bb4
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=54, start=start, end=start + 0.75))  # D5
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=start, end=start + 0.75))  # F5
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=51, start=start, end=start + 0.75))  # Ab4
    elif bar == 4:
        # Cm7 (C, Eb, G, Bb)
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=start, end=start + 0.75))  # C5
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=start, end=start + 0.75))  # Eb5
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.75))  # G5
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=start, end=start + 0.75))  # Bb4

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),  # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # A4
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),  # Bb4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * bar_length
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    hihat_notes = [
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    ]
    drums.notes.extend([kick1, kick3, snare2, snare4] + hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
