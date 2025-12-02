
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in, sax melody
# F7 - Bb7 - C7 - D7 (open voicings, resolve on last)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),  # F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),

    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),  # Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=3.0),

    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),  # C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),

    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5),  # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.5),
]
piano.notes.extend(piano_notes)

# Bass line: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=3.0),  # A (F5)
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.75),  # G (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),  # A (F5)
]
bass.notes.extend(bass_notes)

# Sax melody: motif starting on F7, open and lingering
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=87, start=1.5, end=1.875),  # F7 (F)
    pretty_midi.Note(velocity=110, pitch=89, start=2.25, end=2.625),  # Bb7 (Bb)
    pretty_midi.Note(velocity=110, pitch=92, start=3.0, end=3.375),  # C7 (C)
    pretty_midi.Note(velocity=110, pitch=95, start=3.75, end=4.125),  # D7 (D)
]
sax.notes.extend(sax_notes)

# Bar 2-4 drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3 of each bar
    for beat in [0, 2]:
        kick_start = start + beat * 0.375
        kick_end = kick_start + 0.375
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    # Snare on 2 and 4
    for beat in [1, 3]:
        snare_start = start + beat * 0.375
        snare_end = snare_start + 0.375
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    # Hi-hat on every eighth
    for beat in range(0, 4):
        hihat_start = start + beat * 0.375
        hihat_end = hihat_start + 0.375
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
