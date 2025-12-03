
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # F5
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=1.875),  # A5
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.375),  # F5
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.625),   # A5
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # F5
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.375),  # A5
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.625),  # Bb5
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.875)  # F5
]
sax.notes.extend(sax_notes)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.625),   # F2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.0),   # Ab2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=38, start=2.5, end=2.625),   # F2
    pretty_midi.Note(velocity=90, pitch=41, start=2.875, end=3.0),   # Ab2
    pretty_midi.Note(velocity=90, pitch=43, start=3.25, end=3.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=38, start=3.5, end=3.625),   # F2
    pretty_midi.Note(velocity=90, pitch=41, start=3.875, end=4.0),   # Ab2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),   # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.625),   # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),   # C5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.625),   # E5
]
# Bar 3: Bb7 (Bb D F A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.375),  # A4
])
# Bar 4: C7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.125),   # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125),   # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.125),   # B4
])
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
