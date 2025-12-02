
import pretty_midi

# Initialize the MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
# Note durations: 0.375s per beat, 1.5s per bar

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),   # Kick on beat 1
    (38, 0.375, 0.375), # Snare on beat 2
    (42, 0.0, 0.1875),  # Hihat on 1 & 1/8
    (42, 0.1875, 0.1875), # Hihat on 1/8 & 2/8
    (42, 0.375, 0.1875), # Hihat on 2/8 & 3/8
    (42, 0.5625, 0.1875), # Hihat on 3/8 & 4/8
    (36, 0.75, 0.375),  # Kick on beat 3
    (38, 1.125, 0.375), # Snare on beat 4
    (42, 0.75, 0.1875),  # Hihat on 3 & 3/8
    (42, 0.9375, 0.1875), # Hihat on 3/8 & 4/8
    (42, 1.125, 0.1875), # Hihat on 4/8 & 1/16
    (42, 1.3125, 0.1875) # Hihat on 1/16 end
]

for note, start, duration in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Key: Fm (F, Ab, Bb, Db, Eb, Gb, Ab)
# Bar 2: sax starts at 1.5s with a 4-note motif in Fm
# Motif: F, Ab, Bb, Eb (melodic, slightly chromatic)
# Each note is 0.375s (1 beat), start at 1.5s
sax_notes = [
    (84, 1.5, 0.375),  # F (tenor sax is transposed: F on sax is Bb in concert, but we're in Fm here)
    (81, 1.875, 0.375), # Ab (transposed)
    (80, 2.25, 0.375),  # Bb
    (78, 2.625, 0.375)  # Eb
]
for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Marcus on bass (walking line in Fm)
# Notes: F, Gb, Ab, Bb, F, Gb, Ab, Bb (repeat for 3 bars)
bass_notes = []
bass_start = 1.5
bass_notes = [
    (53, bass_start, 0.375),   # F (bass)
    (52, bass_start + 0.375, 0.375), # Gb
    (51, bass_start + 0.75, 0.375),  # Ab
    (50, bass_start + 1.125, 0.375), # Bb
    (53, bass_start + 1.5, 0.375),   # F
    (52, bass_start + 1.875, 0.375), # Gb
    (51, bass_start + 2.25, 0.375),  # Ab
    (50, bass_start + 2.625, 0.375), # Bb
    (53, bass_start + 3.0, 0.375),   # F
    (52, bass_start + 3.375, 0.375), # Gb
    (51, bass_start + 3.75, 0.375),  # Ab
    (50, bass_start + 4.125, 0.375), # Bb
    (53, bass_start + 4.5, 0.375),   # F
    (52, bass_start + 4.875, 0.375), # Gb
    (51, bass_start + 5.25, 0.375),  # Ab
    (50, bass_start + 5.625, 0.375)  # Bb
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Diane on piano: 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, Db (2nd bar)
# Gbm7: Gb, Bb, Db, F (3rd bar)
# Abm7: Ab, Bb, Db, Eb (4th bar)
# Chords on beat 2 and 4 of each bar
piano_notes = []
piano_start = 1.5
chords = [
    # Bar 2 (1.5 - 2.25s): Fm7 on beat 2 and 4
    (64, 1.875, 0.375),  # F (Fm7)
    (61, 1.875, 0.375),  # Ab
    (60, 1.875, 0.375),  # Bb
    (58, 1.875, 0.375),  # Db
    (64, 2.25, 0.375),   # F
    (61, 2.25, 0.375),   # Ab
    (60, 2.25, 0.375),   # Bb
    (58, 2.25, 0.375),   # Db
    # Bar 3 (2.25 - 3.0s): Gbm7 on beat 2 and 4
    (62, 2.625, 0.375),  # Gb
    (60, 2.625, 0.375),  # Bb
    (58, 2.625, 0.375),  # Db
    (64, 2.625, 0.375),  # F
    (62, 3.0, 0.375),    # Gb
    (60, 3.0, 0.375),    # Bb
    (58, 3.0, 0.375),    # Db
    (64, 3.0, 0.375),    # F
    # Bar 4 (3.0 - 3.75s): Abm7 on beat 2 and 4
    (65, 3.375, 0.375),  # Ab
    (60, 3.375, 0.375),  # Bb
    (58, 3.375, 0.375),  # Db
    (62, 3.375, 0.375),  # Eb
    (65, 3.75, 0.375),   # Ab
    (60, 3.75, 0.375),   # Bb
    (58, 3.75, 0.375),   # Db
    (62, 3.75, 0.375)    # Eb
]
for note, start, duration in piano_notes + chords:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save to a MIDI file
midi.write("dante_russo_intro.mid")
print("MIDI file generated: 'dante_russo_intro.mid'")
