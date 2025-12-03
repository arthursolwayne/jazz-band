
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

# Kick on 1 and 3
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.append(drum_kick)
drums.notes.append(drum_kick2)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.append(drum_snare)
drums.notes.append(drum_snare2)

# Hihat on every eighth note
for i in range(0, 4):
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=i * 0.375, end=i * 0.375 + 0.1875)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, D2 to G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0),  # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, chord each bar, resolve on last
# Bar 2: D7 (D F# A C)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Bb4
]
piano.notes.extend(piano_notes_bar2)

# Bar 3: Bm7b5 (B D F A)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # A4
]
piano.notes.extend(piano_notes_bar3)

# Bar 4: Gmaj7 (G B D F#)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb4
]
piano.notes.extend(piano_notes_bar4)

# You: Sax, one short motif, start it, leave it hanging, come back and finish it

# Bar 2: Start motif
sax_note1 = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875)  # B4
sax.notes.append(sax_note1)

# Bar 3: Leave it hanging
sax_note2 = pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625)  # B4
sax.notes.append(sax_note2)

# Bar 4: Finish it
sax_note3 = pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375)  # B4
sax_note4 = pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75)  # G4
sax_note5 = pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125)  # G4
sax_note6 = pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5)  # A4
sax_note7 = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875)  # G4
sax_note8 = pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25)  # G4
sax_note9 = pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625)  # A4
sax_note10 = pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0)  # G4

sax.notes.extend([sax_note3, sax_note4, sax_note5, sax_note6, sax_note7, sax_note8, sax_note9, sax_note10])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
