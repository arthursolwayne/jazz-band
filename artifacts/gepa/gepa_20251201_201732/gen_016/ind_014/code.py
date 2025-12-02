
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, roots and fifths with chromatic approaches (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (Bar 2, 1)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2 (Bar 2, 2)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2 (Bar 2, 3)
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # F2 (Bar 2, 4)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2 (Bar 3, 1)
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # Eb2 (Bar 3, 2)
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # F2 (Bar 3, 3)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # G2 (Bar 3, 4)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2 (Bar 4, 1)
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # Eb2 (Bar 4, 2)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # G2 (Bar 4, 3)
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)   # F2 (Bar 4, 4)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # C#5
]
# Bar 3: Bm7 (B-D-F#-A)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # F#5
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # A5
])
# Bar 4: A7 (A-C#-E-G)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A5
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # C#6
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # E6
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # G6
])
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - D4 (saxophone range: D4 is 62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4 (Bar 2, 1)
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # F#4 (Bar 2, 2)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D4 (Bar 2, 3)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4 (Bar 4, 1)
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # F#4 (Bar 4, 2)
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25)   # D4 (Bar 4, 3)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4 (same pattern as bar 1, repeated)
for i in range(2):
    for note in drum_notes:
        new_note = pretty_midi.Note(
            velocity=note.velocity,
            pitch=note.pitch,
            start=note.start + 1.5 + (i + 1) * 3.0,
            end=note.end + 1.5 + (i + 1) * 3.0
        )
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
