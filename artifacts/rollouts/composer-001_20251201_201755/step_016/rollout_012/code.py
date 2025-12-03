
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=2.0),   # D2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=2.0, end=2.5),   # F (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=3.0),   # A (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.5),   # G (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.5, end=4.0),   # D2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=4.0, end=4.5),   # F (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=5.0),   # A (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=5.0, end=5.5),   # G (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=5.5, end=6.0),   # D2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),   # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),   # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),   # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),   # C5
]
# Bar 3: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),   # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),   # D4
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.5),   # F5
])
# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),   # C4
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=3.0),   # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),   # G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),   # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),   # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.5),   # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),   # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.5),   # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=6.0),   # Bb4
])
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 2
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75))
    # Snare on 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Hihat on 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5))
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - A4 - D5 (ascending third interval)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),   # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),   # F4
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),   # A4
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.5),   # D5 (leave it hanging)
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),   # A4
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),   # F4
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),   # D4
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),   # D4 (resolve)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
