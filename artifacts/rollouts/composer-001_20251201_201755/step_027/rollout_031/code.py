
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches

# Bar 2 (1.5 - 3.0s)
bass_notes = [
    # Fm root (F2, 53) on beat 1
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),
    # Bb (Bb2, 57) on beat 2
    pretty_midi.Note(velocity=80, pitch=57, start=1.875, end=2.25),
    # D (D2, 50) on beat 3
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),
    # Ab (Ab2, 55) on beat 4
    pretty_midi.Note(velocity=80, pitch=55, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=3.0)   # Eb
]
piano.notes.extend(piano_notes)

# Bar 3 (3.0 - 4.5s): Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5)   # Ab
]
piano.notes.extend(piano_notes)

# Bar 4 (4.5 - 6.0s): Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0)   # Bb
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for i in range(8):
        start_time = start + (i * 0.1875)
        end_time = start + (i * 0.1875) + 0.1875
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start_time, end=end_time)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2 (1.5 - 3.0s): Fm melodic idea
# F (F4, 72), Ab (Ab4, 75), C (C5, 76), Ab (Ab4, 75) - leave it hanging on Ab
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=75, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=76, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=75, start=2.25, end=2.5)
]
sax.notes.extend(sax_notes)

# Bar 3 (3.0 - 4.5s): Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=75, start=3.25, end=3.5)
]
sax.notes.extend(sax_notes)

# Bar 4 (4.5 - 6.0s): Finish motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=76, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=75, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.5),
    pretty_midi.Note(velocity=110, pitch=75, start=5.5, end=5.75),
    pretty_midi.Note(velocity=110, pitch=72, start=5.75, end=6.0)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
