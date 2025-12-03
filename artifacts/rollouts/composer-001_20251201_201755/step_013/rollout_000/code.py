
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
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in F (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# F7: D (38), F (41), A (45), Bb (46)
# Bar 2: F7
note = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75)  # D2 (chromatic approach)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=41, start=1.75, end=2.0)   # F2 (root)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=45, start=2.0, end=2.25)  # A2 (fifth)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=46, start=2.25, end=2.5)  # Bb2 (bass note)
bass.notes.append(note)

# Bar 3: Bb7
note = pretty_midi.Note(velocity=100, pitch=40, start=2.5, end=2.75)  # G2 (chromatic approach)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=46, start=2.75, end=3.0)   # Bb2 (root)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25)  # D3 (fifth)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=51, start=3.25, end=3.5)  # Eb3 (bass note)
bass.notes.append(note)

# Bar 4: C7
note = pretty_midi.Note(velocity=100, pitch=43, start=3.5, end=3.75)  # B2 (chromatic approach)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.0)   # C3 (root)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=52, start=4.0, end=4.25)  # E3 (fifth)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=53, start=4.25, end=4.5)  # F3 (bass note)
bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, Eb) - Open voicing
note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0)  # F4
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=2.0)  # A4
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0)  # C5
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0)  # Bb4
piano.notes.append(note)

# Bar 3: Bb7 (Bb, D, F, Ab) - Open voicing
note = pretty_midi.Note(velocity=100, pitch=61, start=2.5, end=3.0)  # Bb4
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0)  # D4
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0)  # F4
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0)  # Eb4
piano.notes.append(note)

# Bar 4: C7 (C, E, G, Bb) - Open voicing
note = pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=4.0)  # C4
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=4.0)  # E4
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0)  # G4
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=4.0)  # Bb4
piano.notes.append(note)

# You: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), G (67), Bb (69), F (65)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0)
sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
