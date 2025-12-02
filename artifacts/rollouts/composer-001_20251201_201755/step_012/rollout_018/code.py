
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (F root)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # A2 (F5)
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),   # G#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2 (F root)
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # A2 (F5)
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),   # G#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2 (F root)
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # A2 (F5)
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),   # G#2 (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A (76)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # C (79)
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),  # E (82)
]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F
])
# Bar 4: C7 (C, E, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # Bb
])
for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75))
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125))
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5))
for note in drum_notes:
    drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 (F, A, C, Eb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=79, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=74, start=2.625, end=3.0),   # Eb
    pretty_midi.Note(velocity=110, pitch=76, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=79, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=110, pitch=76, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=79, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),   # F
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
