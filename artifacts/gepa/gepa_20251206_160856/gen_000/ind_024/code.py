
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full band in
# Sax melody: Dm7 -> G7 -> Cm7 -> F7
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=110, pitch=74, start=2.625, end=3.0),  # C
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # C
]
# Bar 3: G7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625), # F#
])
# Bar 4: Cm7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0), # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0), # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0), # Bb
])
piano.notes.extend(piano_notes)

# Bar 3 and 4: Drums continue with same pattern
for i in range(3):
    for note in drum_notes:
        note.start += 1.5
        note.end += 1.5
        drums.notes.append(note)

# Bar 3: Sax continues with motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625), # C2
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),  # Bb2
]
bass.notes.extend(bass_notes)

# Bar 4: Drums end on 4
# No new notes, just repeat the pattern

# Bar 4: Sax ends on C
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=2.625, end=3.0), # C
]
sax.notes.extend(sax_notes)

# Bar 4: Bass resolves on D2
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0), # D2
]
bass.notes.extend(bass_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
