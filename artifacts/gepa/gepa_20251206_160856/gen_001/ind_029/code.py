
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),  # Fm root
    pretty_midi.Note(velocity=100, pitch=41, start=1.75, end=2.0),  # Ab (fifth)
    pretty_midi.Note(velocity=100, pitch=39, start=2.0, end=2.25),  # G (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.5),  # G#
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=2.75, end=3.0),  # Ab

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.25),  # C (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=3.25, end=3.5),  # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=41, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=43, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=42, start=4.25, end=4.5),  # Bb

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=39, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.5),  # G#
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=5.75, end=6.0),  # Ab
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Bar 2 (1.5 - 3.0s): Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=3.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=3.0),   # Ab

    # Bar 3 (3.0 - 4.5s): Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=56, start=3.0, end=4.5),   # Ab

    # Bar 4 (4.5 - 6.0s): Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),   # A
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),   # E
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),   # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - one short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Motif: F (53), G (55), Ab (56), F (53) -> introduce on bar 2, leave on bar 3, return on bar 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=56, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.5),  # F

    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # F (return)
    pretty_midi.Note(velocity=100, pitch=55, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=56, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.0),  # F

    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.75),  # F (finish)
    pretty_midi.Note(velocity=100, pitch=55, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=56, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.5),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    for i in range(4):
        time = bar_start + i * 0.375
        if i == 0 or i == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))  # kick
        elif i == 1 or i == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375))  # snare
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375))    # hihat

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
