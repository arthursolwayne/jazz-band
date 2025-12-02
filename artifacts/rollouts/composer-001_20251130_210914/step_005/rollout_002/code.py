
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=70, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in D, chromatic approaches, never the same note twice
# D minor scale: D, Eb, F, G, Ab, Bb, B
# Walking bass line
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 50),  # D
    (1.875, 48), # Eb
    (2.25, 52),  # F
    (2.625, 55), # G
    (3.0, 46),  # Ab
    # Bar 3 (3.0 - 4.5s)
    (3.375, 44), # Bb
    (3.75, 50),  # D
    (4.125, 48), # Eb
    (4.5, 55),  # G
    # Bar 4 (4.5 - 6.0s)
    (4.875, 52), # F
    (5.25, 46),  # Ab
    (5.625, 50), # D
    (6.0, 52)    # F
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4, comp on 2 and 4
# D minor 7th: D, F, A, C
# D minor 7 flat 5: D, F, Ab, C
# D minor 7 flat 13: D, F, Ab, Bb, C
# Bars 2-4
for bar in range(2, 5):
    time = (bar - 2) * 1.5 + 0.75  # On 2 and 4 of each bar
    if bar % 2 == 0:
        # Dm7 flat 5
        midi_notes = [50, 52, 46, 57]
    else:
        # Dm7 flat 13
        midi_notes = [50, 52, 46, 49, 57]
    for note in midi_notes:
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
        piano.notes.append(piano_note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=70, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Dante: Tenor sax, one motif, make it sing
# Motif: D, F, Bb, Ab (D minor 7 flat 13)
# Start on bar 2, 1st beat
# 1st note: D (62)
# 2nd note: F (65)
# 3rd note: Bb (67)
# 4th note: Ab (66)
# Leave it hanging on Ab at the end, come back and finish it

# First pass: play motif
sax_notes = [
    (1.5, 62, 0.5),  # D
    (2.0, 65, 0.5),  # F
    (2.5, 67, 0.5),  # Bb
    (3.0, 66, 0.5),  # Ab
]
for time, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Second pass: return to finish the motif
sax_notes = [
    (4.5, 62, 0.5),  # D
    (5.0, 65, 0.5),  # F
    (5.5, 67, 0.5),  # Bb
    (6.0, 66, 0.5),  # Ab
]
for time, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
